from setuptools import setup, find_packages

setup(
    name="TkinterOS",
    version="0.1",
    description="A Fake Operating System Inspired By GodotOS",
    author="Simon Milata",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        "customtkinter==5.2.2",
        "darkdetect==0.8.0",
        "packaging==25.0",
        "Pillow==11.3.0",
        "playsound==1.2.2",
    ],
    python_requires=">=3.10",
    include_package_data=True,
)