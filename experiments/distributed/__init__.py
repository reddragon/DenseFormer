# Copyright 2023 Matteo Pagliardini, Amirkeivan Mohtashami, Francois Fleuret, Martin Jaggi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from . import ddp
from . import single

BACKEND_TYPE_TO_MODULE_MAP = {
    "nccl": ddp.DataParallelDistributedBackend,
    None: single.SinlgeNodeBackend,
}


def get_backend_class_from_args(args):
    return BACKEND_TYPE_TO_MODULE_MAP[args.distributed_backend]


def make_backend_from_args(args):
    return get_backend_class_from_args(args)(args)


def registered_backends():
    return BACKEND_TYPE_TO_MODULE_MAP.keys()
