import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.note_create import NoteCreate  # noqa: E501
from openapi_server.models.note_list_response import NoteListResponse  # noqa: E501
from openapi_server import util


def notes_get(page=None, per_page=None, q=None):  # noqa: E501
    """List notes (paginated)

     # noqa: E501

    :param page: Page number (1-based)
    :type page: int
    :param per_page: Items per page (1–100)
    :type per_page: int
    :param q: Optional filter string
    :type q: str

    :rtype: Union[NoteListResponse, Tuple[NoteListResponse, int], Tuple[NoteListResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def notes_id_get(id):  # noqa: E501
    """Get note by id

     # noqa: E501

    :param id: Note id
    :type id: int

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    return 'do some magic!'


def notes_post(note_create):  # noqa: E501
    """Create a note

     # noqa: E501

    :param note_create: 
    :type note_create: dict | bytes

    :rtype: Union[Note, Tuple[Note, int], Tuple[Note, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        note_create = NoteCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
