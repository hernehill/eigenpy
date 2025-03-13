name = 'eigenpy'

version = '3.10.3.hh.1.0.0'

authors = [
    'eigenPy',
]

description = '''Python wrapper for the C++ Eigen Linear Algebra library'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']

requires = [
    "boost-1.82",
    "eigen-3",
    "scipy",
]

private_build_requires = [
]

variants = [
    # ["python-3.7", "numpy-1.21.6"],
    ["python-3.9", "numpy-1.26.4"],
    ["python-3.10", "numpy-1.26.4"],
    ["python-3.11", "numpy-1.26.4"],
    ["python-3.12", "numpy-1.26.4"],
]

def commands():
    env.REZ_EIGENPY_ROOT = '{root}'

    env.LD_LIBRARY_PATH.append("{root}/lib64")

    python_dir = f"python{resolve.python.version.major}.{resolve.python.version.minor}"
    packages_dir = "{root}/lib"
    packages_dir += f"/{python_dir}/site-packages"

    env.PYTHONPATH.append(packages_dir)

uuid = 'repository.eigenpy'
