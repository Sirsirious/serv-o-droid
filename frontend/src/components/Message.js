
import React from 'react';

const Message = ({chat, user}) => (
    <div className={`chat ${user === chat.username ? "right" : "left"}`} key={chat.id}>
        {user !== chat.username
            && <img src='https://cdn-icons-png.flaticon.com/512/3662/3662817.png' alt={`${chat.username}'s profile pic`} />
        }
        {user === chat.username ? "You: "+chat.content: "Agent: "+chat.content}
    </div>
);

export default Message;