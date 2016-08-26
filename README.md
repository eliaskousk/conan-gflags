[![Build Status](https://travis-ci.org/eliaskousk/conan-gflags.svg)](https://travis-ci.org/eliaskousk/conan-gflags)


# conan-gflags

[Conan.io](https://conan.io) package for Google's GFlags library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/gflags/2.1.2/eliaskousk/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload gflags/2.1.2@eliaskousk/stable --all

## Reuse the packages

### Basic setup

    $ conan install gflags/2.1.2@eliaskousk/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    gflags/2.1.2@eliaskousk/stable

    [options]
    gtest:shared=true # false

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:

    conan install .

Project setup installs the library (and all his dependencies) and generates the files
*conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that
you need to link with your dependencies.
