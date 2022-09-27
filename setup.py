from setuptools import find_packages, setup

install_requires = open("./requirements/requirements.txt").read().strip().split("\n")

# gpu_requires = open("./requirements/requirements.gpu.txt").read().strip().split("\n")
# extras = {
#     'gpu': gpu_requires
# }

#extras["all_extras"] = sum(extras.values(), [])

setup(
    name="wafer-classified-as-cnn",
    version='0.0.1',
    author="Jo Yong Sik",
    entry_points={
          'console_scripts': []
      },
    python_requires=">=3.7",
    dependency_links=[
        "https://download.pytorch.org/whl/torch_stable.html",
        "https://download.pytorch.org/whl/cu113"
        ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires='',
    # extras_require=extras,
    setup_requires=['pytest-runner']
)
