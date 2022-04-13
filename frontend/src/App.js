import './App.css';
import Chatroom from './routes/Chatroom.js';
import ChatroomList from './routes/ChatroomList.js';
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link
} from "react-router-dom";
import Home from "./routes/Home";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import {NavDropdown} from "react-bootstrap";

function App() {
    return (
        <Router>
            <div>
                <Navbar bg="light" expand="lg" variant="light">
                    <Navbar.Brand as={Link} to="/">
                        <img
                            alt=""
                            src={'https://cdn-icons-png.flaticon.com/512/3662/3662817.png'}
                            width="30"
                            height="30"
                            className="d-inline-block align-top"
                        />{' '}
                        Serv-o-droid

                    </Navbar.Brand>
                    <Navbar.Collapse>
                        <Nav className="me-auto">
                            <Nav.Link as={Link} to='/chatrooms'> Chatrooms </Nav.Link>
                            <Nav.Link as={Link} to='/manage_chatrooms'> Manage Chatrooms </Nav.Link>
                        </Nav>
                        <Nav className="p-2 flex-fill bd-highlight">
                            <NavDropdown title="NLU">
                                <Nav.Link as={Link} to='/models'> Models </Nav.Link>
                                <Nav.Link as={Link} to='/datasets'> Datasets </Nav.Link>
                                <Nav.Link as={Link} to='/intents'> Intents </Nav.Link>
                            </NavDropdown>

                        </Nav>
                    </Navbar.Collapse>
                </Navbar>
                <Routes>
                    <Route path="/chatrooms" element={<ChatroomList/>}/>
                    <Route path="/chatrooms/:chatroomId" element={<Chatroom/>}/>
                    <Route path="/" element={<Home/>}/>
                </Routes>
            </div>
        </Router>
    );
}


export default App;
