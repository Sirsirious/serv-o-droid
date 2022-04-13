import React from 'react';
import ReactDOM from 'react-dom';
import '../App.css';
import {withRouter} from "../utils/withRouter";
import Message from '../components/Message.js';


class Chatroom extends React.Component {
    constructor(props) {
        super(props);
        this.state = {chats: []};

        this.submitMessage = this.submitMessage.bind(this);
        this.componentDidMount = this.componentDidMount.bind(this);
        this.getConversationMessages = this.getConversationMessages.bind(this);
        this.render = this.render.bind(this);
    }

    componentDidMount() {
        let chatroomId = this.props.router.params.chatroomId;
        this.getConversationMessages(chatroomId);
        this.scrollToBot();
    }

    componentDidUpdate() {
        this.scrollToBot();
    }

    scrollToBot() {
        ReactDOM.findDOMNode(this.refs.chats).scrollTop = ReactDOM.findDOMNode(this.refs.chats).scrollHeight;
    }

    async submitMessage(e) {
        e.preventDefault();
        const message_success = await this.sendConversationMessage(ReactDOM.findDOMNode(this.refs.msg).value);
        message_success && this.setState({
            chats: this.state.chats.concat([{
                id: '',
                conversation_id: '',
                posted_at: '',
                username: "user",
                content: message_success
            }])
        }, () => {
            ReactDOM.findDOMNode(this.refs.msg).value = "";
        });
    }

    async sendConversationMessage(message) {
        let chatroomId = this.props.router.params.chatroomId;
        return await fetch(`http://127.0.0.1:8000/conversations/${chatroomId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: message,
                from_agent: false
            })
        }).then(res => { return res.status===200? message: null});

    }

    async getConversationMessages(conversation_id) {
        return fetch(`http://127.0.0.1:8000/conversations/messages/${conversation_id}`)
            .then(response => response.json())
            .then(data => {
                return data.map(message => ({
                    id: message.id,
                    conversation_id: conversation_id,
                    username: message.from_agent ? "bot" : "user",
                    content: message.text,
                    posted_at: message.posted_at
                }));
            }).then(chats => {
                this.setState({chats: chats});
            });
    }

    render() {
        const username = "user";
        const {chats} = this.state;

        return (
            // Create a centered div using bootstrap


                <div className="col-md-12">

                    <div className="chatroom panel-body">
                        <h3>Serv-o-droid</h3>
                        <div className="chats" ref="chats">
                            {chats &&
                                chats.map((chat) =>
                                    <Message chat={chat} user={username}/>
                                )
                            }
                        </div>
                        <form className="input" onSubmit={(e) => this.submitMessage(e)}>
                            <input type="text" ref="msg"/>

                            <input type="submit" value="Submit" disabled={this.state.chats.at(-1) && this.state.chats.at(-1).username !== "bot"}
                            title={this.state.chats.at(-1) && this.state.chats.at(-1).username !== "bot"? "You must wait the agent response to send a message.": ""}/>
                        </form>
                    </div>


                </div>

        );
    }
}

export default withRouter(Chatroom);