from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans.tools import cpu_count
from conans import CMake

class GFlagsConan(ConanFile):
    name = "gflags"
    version = "2.2.0"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fpic": [True, False]}
    default_options = "shared=False", "fpic=True"
    exports="CMakeLists.txt", "FindGflags.cmake", "change_dylib_names.sh"
    url="http://github.com/eliaskousk/conan-gflags"
    license="https://github.com/gflags/gflags/blob/master/COPYING.txt"
    zip_folder_name = "gflags-%s" % version

    def source(self):
        zip_name = "v%s.tar.gz" % self.version
        url = "https://github.com/gflags/gflags/archive/%s" % zip_name
        download(url, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
        jobs = ""
        if self.settings.os == "Windows":
            self.run("IF not exist _build mkdir _build")
        else:
            self.run("mkdir _build")
            jobs = "-- -j%s" % (cpu_count() + 1)
        cd_build = "cd _build"
        shared = "-DBUILD_SHARED_LIBS=1" if self.options.shared else ""
        fpic = "-DCMAKE_POSITION_INDEPENDENT_CODE=TRUE" if self.options.fpic else ""
        self.run("%s && cmake .. %s %s %s" % (cd_build, cmake.command_line, shared, fpic))
        self.run("%s && cmake --build . %s %s" % (cd_build, cmake.build_config, jobs))

    def package(self):

        if self.settings.os == "Macos" and self.options.shared:
            self.run("bash ./change_dylib_names.sh")

        # Copy findgflags script into project
        self.copy("FindGflags.cmake", ".", ".")

        # Copying headers
        incdir = "_build/%s/include" % self.zip_folder_name
        self.copy(pattern="*.h", dst="include", src=incdir, keep_path=True)

        if self.options.shared:
            # Copying dynamic libs
            libdir = "_build/%s" % self.zip_folder_name
            self.copy(pattern="*.so*", dst="lib", src=libdir, keep_path=False)
            self.copy(pattern="*.dylib*", dst="lib", src=libdir, keep_path=False)
            self.copy(pattern="*.dll", dst="bin", src=libdir, keep_path=False)
        else:
            # Copying static libs
            libdir = "_build/lib"
            self.copy(pattern="*.a", dst="lib", src=libdir, keep_path=False)

        self.copy(pattern="*.lib", dst="lib", src=libdir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['gflags']

        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

