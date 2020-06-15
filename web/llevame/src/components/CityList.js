import React, { Component } from 'react';
import CityOption from './CityOption';

export class CityList extends Component {
    render() {
        return this.props.cityList.map((city) => (
            <CityOption key={city.id} city={city} />
        ));
    };
}

export default CityList
