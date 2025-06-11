from setuptools import setup, find_packages

setup(
    name="FleetDefenseSim",
    version="0.1.0",
    description="A short description of your package",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/FleetDefense",
    package_dir={"FleetDefenseSim": "FleetDefenseSim/src/sim"},
    packages=["FleetDefenseSim"],
    install_requires=["pandas", "pydantic", "numpy", "scipy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
