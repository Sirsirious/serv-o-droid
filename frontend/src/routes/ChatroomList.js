import React from 'react';
import '../App.css';
import ChatroomEntry from "../components/ChatroomEntry";


class ChatroomList extends React.Component {
    constructor(props) {
        super(props);

        this.state = {chats: []};
    }

    componentDidMount() {
        this.getConversations();
    }


    getConversations() {
        return fetch(`http://127.0.0.1:8000/conversations`)
            .then(response => {
                return response.json();
            })
            .then(chats => {
                this.setState({chats: chats});
            });
    }

    render() {
        const {chats} = this.state;

        return (
            // Generate a centered page with a div named chatrooms using bootstrap
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <h1>Chatrooms</h1>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-12">
                        <div className="list-group">
                            {chats &&
                                chats.map((chat) =>
                                    <ChatroomEntry chatdata={chat}/>
                                )
                            }
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default ChatroomList;
