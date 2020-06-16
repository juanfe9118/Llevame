import React, { Component } from 'react'

export class CityOption extends Component {
    render() {
        return (
            <React.Fragment>
                <option value={this.props.city.name}>{this.props.city.name}</option>
            </React.Fragment>
        )
    }
}

export default CityOption
