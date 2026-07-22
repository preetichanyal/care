from plugs.manager import PlugManager
from plugs.plug import Plug  # noqa: F401

"""abdm_plug = Plug(
    name="abdm",
    package_name="git+https://github.com/10bedicu/care_abdm.git",
    version="@develop",
    configs={
    },
)"""

abdm_plug = Plug(
    name="abdm",
    package_name="git+https://github.com/preetichanyal/care_abdm.git",
    version="@abdm_code_changes",
)

plugs = [abdm_plug]

manager = PlugManager(plugs)
