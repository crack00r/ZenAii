from .req_pq import ReqPqRequest
from .req_dh_params import ReqDHParamsRequest
from .set_client_dh_params import SetClientDHParamsRequest
from .destroy_auth_key import DestroyAuthKeyRequest
from .rpc_drop_answer import RpcDropAnswerRequest
from .get_future_salts import GetFutureSaltsRequest
from .ping import PingRequest
from .ping_delay_disconnect import PingDelayDisconnectRequest
from .destroy_session import DestroySessionRequest
from .invoke_after_msg import InvokeAfterMsgRequest
from .invoke_after_msgs import InvokeAfterMsgsRequest
from .init_connection import InitConnectionRequest
from .invoke_with_layer import InvokeWithLayerRequest
from .invoke_without_updates import InvokeWithoutUpdatesRequest
from . import payments, messages, account, bots, photos, help, upload, channels, users, stickers, contest, contacts, phone, auth, updates, langpack
