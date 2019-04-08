#     Copyright 2019, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
from package1.module1 import module1_f1
from package1.module2 import module2_f1
from package1.subpackage2.submodule21 import submodule21_f1
from package1.subpackage1.submodule11 import submodule11_f2


def main():
  module1_f1('package1.main.py')
  module2_f1('package1.main.py')
  submodule11_f2('package1.main.py')
  submodule21_f1('package1.main.py')
