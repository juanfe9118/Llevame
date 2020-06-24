import React, { Component } from 'react';
import DepOption from './DepOption';

export class DepList extends Component {
    render() {
        return this.props.depList.map((dep) => (
            <DepOption key={dep.id} dep={dep} />
        )); 
    };
}

export default DepList
