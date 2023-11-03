import React, { Component } from 'react';

class ClassInput extends Component {
    //Some code goes here

    //Each class requires a constructor
    constructor(props) {
        super(props);
        this.state = { value: '' };
    }

    //Each class requires a render function
    render() {
        return (
            <div>
                <input type="text" value={this.state.value} onChange={this.handleChange} />
                <p>{this.state.value}</p>
            </div>
        );
    }
}

export default ClassInput;