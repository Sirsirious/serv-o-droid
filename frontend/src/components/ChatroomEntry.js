import React from 'react';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { Link } from "react-router-dom";

const ChatroomEntry = ({chatdata}) => (
    // Generate a item for each chatdata using bootstrap accordions
    <Row>
        <Col>
            <div className="accordion" id="accordionExample">
                <div className="card">
                    <div className="card-header" id="headingOne">
                        <h2 className="mb-0">
                            Chat with id {chatdata.id}
                        </h2>
                    </div>
                    <div id={`collapse${chatdata.id}`} className="collapse show" aria-labelledby="headingOne" data-parent="#accordionExample">
                        <div className="card-body">
                            <p>Chat started at: {chatdata.started_at}</p>
                            <br/>
                            <Link to={`/chatrooms/${chatdata.id}`}>
                                <button className="btn btn-primary">Open Chatroom</button>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </Col>
    </Row>

);

export default ChatroomEntry;