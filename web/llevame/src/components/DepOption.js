import React, { Component } from 'react'

export class DepOption extends Component {
    render() {
        return (
            <React.Fragment>
                <option value={this.props.dep.name}>{this.props.dep.name}</option>
            </React.Fragment>
        )
    }
}

export default DepOption
