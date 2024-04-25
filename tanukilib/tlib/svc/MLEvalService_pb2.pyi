from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Data(_message.Message):
    __slots__ = ("data_value", "data_type")
    DATA_VALUE_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    data_value: str
    data_type: str
    def __init__(self, data_value: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...

class InputData(_message.Message):
    __slots__ = ("data_path", "data")
    DATA_PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data_path: str
    data: _containers.RepeatedCompositeFieldContainer[Data]
    def __init__(self, data_path: _Optional[str] = ..., data: _Optional[_Iterable[_Union[Data, _Mapping]]] = ...) -> None: ...

class MLEval(_message.Message):
    __slots__ = ("model_name", "input")
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    model_name: str
    input: InputData
    def __init__(self, model_name: _Optional[str] = ..., input: _Optional[_Union[InputData, _Mapping]] = ...) -> None: ...

class Outcome(_message.Message):
    __slots__ = ("code", "msg", "data")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: int
    msg: str
    data: str
    def __init__(self, code: _Optional[int] = ..., msg: _Optional[str] = ..., data: _Optional[str] = ...) -> None: ...
