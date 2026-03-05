"""
Mock google.colab module for local Jupyter environment.
Allows notebooks written for Google Colab to run locally without any code changes.
"""

import os
import functools
import builtins

# Colab drive path prefixes to intercept (most specific first)
_COLAB_PREFIXES = [
    '/content/drive/MyDrive/Colab Notebooks/',
    '/content/drive/MyDrive/ColabNotebooks/',
    '/content/drive/MyDrive/',
    '/content/drive/',
]

_project_root = None
_patched = False


def _find_project_root():
    """Find the git root starting from CWD, fallback to CWD."""
    path = os.getcwd()
    while path != os.path.dirname(path):
        if os.path.isdir(os.path.join(path, '.git')):
            return path
        path = os.path.dirname(path)
    return os.getcwd()


def _resolve_colab_path(filepath):
    """Translate a Colab drive path to a local file path."""
    global _project_root

    if not isinstance(filepath, str):
        return filepath

    if not filepath.startswith('/content/'):
        return filepath

    # Find which prefix matches
    rel_path = None
    for prefix in _COLAB_PREFIXES:
        if filepath.startswith(prefix):
            rel_path = filepath[len(prefix):]
            break

    if rel_path is None:
        return filepath

    if _project_root is None:
        _project_root = _find_project_root()

    filename = os.path.basename(rel_path)
    cwd = os.getcwd()

    # 1) Current working directory
    candidate = os.path.join(cwd, filename)
    if os.path.exists(candidate):
        return candidate

    # 2) Project root
    candidate = os.path.join(_project_root, filename)
    if os.path.exists(candidate):
        return candidate

    # 3) data/ subdirectory of project root
    candidate = os.path.join(_project_root, 'data', filename)
    if os.path.exists(candidate):
        return candidate

    # 4) Recursive search in project tree (skip hidden dirs)
    for root, dirs, files in os.walk(_project_root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if filename in files:
            return os.path.join(root, filename)

    print(f"[Colab Compat] WARNING: '{filename}' not found locally")
    return filepath


def _apply_patches():
    """Monkey-patch pandas I/O and builtins.open for Colab path translation."""
    global _patched
    if _patched:
        return
    _patched = True

    # --- Patch pandas.read_csv and read_excel ---
    try:
        import pandas as pd

        for func_name in ('read_csv', 'read_excel', 'read_json', 'read_parquet'):
            if hasattr(pd, func_name):
                orig = getattr(pd, func_name)

                @functools.wraps(orig)
                def _wrapper(filepath_or_buffer, *args, _orig_fn=orig, **kwargs):
                    return _orig_fn(
                        _resolve_colab_path(filepath_or_buffer), *args, **kwargs
                    )

                setattr(pd, func_name, _wrapper)
    except ImportError:
        pass

    # --- Patch builtins.open (only /content/ paths) ---
    _orig_open = builtins.open

    @functools.wraps(_orig_open)
    def _patched_open(file, *args, **kwargs):
        if isinstance(file, str) and file.startswith('/content/'):
            file = _resolve_colab_path(file)
        return _orig_open(file, *args, **kwargs)

    builtins.open = _patched_open


class drive:
    """Mock Google Drive interface."""

    @staticmethod
    def mount(mount_point='/content/drive', force_remount=False):
        global _project_root
        _project_root = _find_project_root()
        _apply_patches()
        print(f"[Colab Compat] Drive mounted (local mode) -> {_project_root}")
