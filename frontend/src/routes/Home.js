import React, {Component} from 'react';

class Home extends Component {
    render() {
        return (
            // Generate centered div using bootstrap with home title
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <h1>Serv-o-droid</h1>
                    </div>
                </div>
            </div>
        );
    }
}

export default Home;