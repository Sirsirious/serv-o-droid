from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal, get_db
from app.database.schemas import conversations_schemas
from app.services import conversations_crud

router = APIRouter(prefix='/conversations')



@router.get('/', tags=['conversations'], response_model=List[conversations_schemas.Conversation])
async def read_conversations(db: Session = Depends(get_db)):
    return conversations_crud.get_conversations(db=db)


@router.get('/{conversation_id}', tags=['conversations'], response_model=conversations_schemas.Conversation)
async def read_conversation(conversation_id: str, db: Session = Depends(get_db)):
    conversation = conversations_crud.get_conversation(db=db, conversation_id=conversation_id)
    if conversation:
        return conversation
    else:
        raise HTTPException(status_code=404, detail=f"Conversation with id {conversation_id} not found")


@router.post('/', tags=['conversations'], response_model=conversations_schemas.Conversation)
async def create_conversation(conversation: conversations_schemas.ConversationCreate,
                              db: Session = Depends(get_db)):
    return conversations_crud.create_conversation(db=db, conversation=conversation)


@router.post('/{conversation_id}', tags=['conversations'], response_model=conversations_schemas.ConversationMessage)
async def add_message_to_conversation(conversation_id: str,
                                      conversation_message: conversations_schemas.ConversationMessageCreate,
                                      db: Session = Depends(get_db)):
    return conversations_crud.create_conversation_message(db=db, conversation_message=conversation_message,
                                                          conversation_id=conversation_id)


@router.get('/messages/{conversation_id}', tags=['conversations'],
            response_model=List[conversations_schemas.ConversationMessage])
async def add_message_to_conversation(conversation_id: str,
                                      db: Session = Depends(get_db)):
    messages = conversations_crud.get_conversation_messages(db=db, conversation_id=conversation_id)
    if not messages:
        raise HTTPException(status_code=404, detail=f"Conversation with id {conversation_id} not found")
    else:
        return messages
