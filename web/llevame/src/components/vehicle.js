import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';

const brands = ['Aston Martin', 'Audi', 'BMW', 'Bugatti', 'Cadillac', 'Chevrolet', 'Dodge', 'Ferrari', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Kia', 'Lamborghini', 'Land Rover', 'Maserati', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mini', 'Mitsubishi', 'Nissan', 'Peugeot', 'Porsche', 'Renault', 'Rolls Royce', 'Saab', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']

const colors = ['White', 'Silver', 'Black', 'Blue', 'Gray', 'Red', 'Green', 'Brown', 'Gold']

function options (arrayOfData) {
    return (arrayOfData.map((data) => <option value={data}>{data}</option>));
}


export default class VehicleRegister extends Component {
    state = {
        plate: '',
        model: '',
        color: '',
        brand: '',
        redirect: '/userlanding',
    }

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    onSubmit = (e) => {
        e.preventDefault();
        const headers = {
            'Authorization': 'Token ' + this.props.token
        }
        axios.post('http://localhost:8000/api/users/' + this.props.user_id +'/vehicles/', {
            "plate": this.state.plate,
            "model": this.state.model,
            "color": this.state.color,
            "brand": this.state.brand,
        }, {headers: headers})
            .then(res => {
                if (res.status === 201) {
                    alert(res.data.response)
                    return <Redirect to={this.state.redirect} />
                }  
            })
            .catch(err => {
                console.log(err)
                let errorDict = err.response.data;
                alert(JSON.stringify(errorDict));
                console.log(err.response.data);
            });
        }
    
    render() {
        return (
            <div id='box'>
                <div id='vehicle_reg'>
                    <h1>New vehicle</h1>
                    <form onSubmit={this.onSubmit}>
                        <input
                            type='text'
                            name='plate'
                            placeholder='plate'
                            value={this.state.plate}
                            onChange={this.onChange}
                            /><br></br>
                        <input
                            type='text'
                            name='model'
                            placeholder='model'
                            value={this.state.model}
                            onChange={this.onChange}
                        /><br></br>
                        <select name='color' onChange={this.onChange}>
                            <option value="" disabled selected>color</option>
                            {options(colors)}
                            onChange={this.onChange}
                        </select><br></br>
                        <select name='brand' onChange={this.onChange}>
                            <option value="" disabled selected>brand</option>
                            {options(brands)}
                        </select>
                        <div id='buttons'>
                            <button onClick={this.backHome}>Cancel</button>
                            <input type='submit' value='Register' />
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}
