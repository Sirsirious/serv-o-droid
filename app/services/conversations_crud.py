from sqlalchemy.orm import Session
from app.database.models import conversations_models
from app.database.schemas import conversations_schemas


# Conversation
def get_conversation(db: Session, conversation_id: str):
    return db.query(conversations_models.Conversation). \
        filter(conversations_models.Conversation.id == conversation_id).first()


def get_conversations(db: Session, limit: int = None):
    if not limit:
        return db.query(conversations_models.Conversation).all()
    else:
        return db.query(conversations_models.Conversation).limit(limit)


def create_conversation(db: Session, conversation: conversations_schemas.ConversationCreate):
    db_conversation = conversations_models.Conversation()
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation


# Conversation messages
def get_conversation_message(db: Session, conversation_message_id: str):
    return db.query(conversations_models.ConversationMessage). \
        filter(conversations_models.ConversationMessage.id == conversation_message_id).first()


def get_conversation_messages(db: Session, conversation_id: str):
    return db.query(conversations_models.ConversationMessage). \
        filter(conversations_models.ConversationMessage.conversation_id == conversation_id).all()


def create_conversation_message(db: Session, conversation_message: conversations_schemas.ConversationMessageCreate,
                                conversation_id: str):
    db_conversation_message = conversations_models.ConversationMessage(**conversation_message.dict(),
                                                                       conversation_id=conversation_id)
    db.add(db_conversation_message)
    db.commit()
    db.refresh(db_conversation_message)
    return db_conversation_message


def update_conversation_message(db: Session, conversation_message: conversations_schemas.ConversationMessageUpdate,
                                conversation_message_id: str):
    db_conversation_message = db.query(conversations_models.ConversationMessage). \
        filter(conversations_models.ConversationMessage.id == conversation_message_id).first()
    if db_conversation_message:
        db_conversation_message.update(conversation_message.dict())
        db.commit()
        db.refresh(db_conversation_message)
        return db_conversation_message
    return None
