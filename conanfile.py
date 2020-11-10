#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import CMake
from conans import ConanFile
from conans.tools import download
from conans.tools import unzip
import os
import shutil

class BoostReflectionConan(ConanFile):
    name = "boost_reflection"
    version = "1.0.1"
    description = "Boost Reflection"
    settings = {"os": ["Linux", "Windows"], "arch": ["x86_64"], "compiler": ["gcc"], "build_type": ["Release", "Debug"]}
    options = {"shared": [True, False]}
    default_options = {
        "shared":False
    }
    requires = "boost/1.72.0"
    generators = "cmake"

    package_name = "boost-reflection-" + version

    def source(self):
        zip_name = self.package_name + ".zip"
        download("https://github.com/jackfive/boost-reflection/archive/v" + self.version + ".zip", zip_name)
        unzip(zip_name)
        shutil.move(self.package_name, "boost-reflection")
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="boost-reflection", build_folder="build")
        cmake.build()

    def package(self):        
        self.copy("*", src="boost", dst="include/boost", keep_path=True)
        self.copy("*.a", dst="lib", src="build/libs/reflection/src", keep_path=False)
        self.copy("*.so", dst="lib", src="build/libs/reflection/src", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["boost_reflection"]

