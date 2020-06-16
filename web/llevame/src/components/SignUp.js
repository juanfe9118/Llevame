import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';
import DepList from './DepList';
import CityList from './CityList';

class SignUp extends Component {
    state = {
        first_name: '',
        last_name: '',
        email: '',
        type_id: '',
        n_document: '',
        city: '',
        department: '',
        password: '',
        confPass: '',
        redirect: null,
        depList: [],
        cityList: [],
    }

    componentDidMount()  {
        axios.get('http://localhost:8000/api/departments/')
            .then(res => {
                this.setState({ depList: res.data.results });
            });
        }

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    depChange = (e) => {
        this.state.depList.map((dep) => {
            if (e.target.value === dep.name) {
                this.setState({department: dep.id});
                axios.get(`http://localhost:8000/api/departments/${dep.id}/cities`)
                    .then(res => {
                        this.setState({cityList: res.data})
                    });
            }
            return dep;
        })
    }

    cityChange = (e) => {
        this.state.cityList.map((city) => {
            if (e.target.value === city.name) {
                this.setState({city: city.id});
            }
            return city;
        });
    }

    onSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/users/', {
            "first_name": this.state.first_name,
            "last_name": this.state.last_name,
            "type_id": this.state.type_id,
            "n_document": this.state.n_document,
            "department": this.state.department,
            "city": this.state.city,
            "picture": null,
            "email": this.state.email,
            "password": this.state.password,
            "password2": this.state.confPass,
        })
            .then(res => {
                if (res.data.response === "User created successfully"){
                    this.setState({ redirect: "/signupconf"})
                    return <Redirect to={this.state.redirect} />
                }
            })
            .catch(err => {
                let errorDict = err.response.data;
                alert(JSON.stringify(errorDict));
                console.log(err.response.data);
            });
    }

    backHome = () => this.setState({ redirect: "/" });

    render() {
        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />
          }
        return (
            <div style={boxStyle}>
                <div style={formStyle}>
                    <h1>Get Started!</h1>
                    <form onSubmit={this.onSubmit}>
                        <input
                            type='text'
                            name='first_name'
                            placeholder='First Name'
                            value={this.state.first_name}
                            onChange={this.onChange}
                        /><br></br>
                        <input
                            type='text'
                            name='last_name'
                            placeholder='Last Name'
                            value={this.state.last_name}
                            onChange={this.onChange}
                        /><br></br>
                        <input
                            type='email'
                            name='email'
                            placeholder='Email'
                            value={this.state.email}
                            onChange={this.onChange}
                        /><br></br>
                        <input
                            list='IdType'
                            name='type_id'
                            placeholder='ID Type'
                            value={this.state.type_id}
                            onChange={this.onChange}
                        />
                        <datalist id='IdType'><option value='CC' /><option value='CE' /><option value='PA' /></datalist>
                        <input
                            type='text'
                            name='n_document'
                            placeholder='ID Number'
                            value={this.state.n_document}
                            onChange={this.onChange}
                        /><br></br>
                        <select name='department' onChange={this.depChange}>
                            <option value="" disabled selected>Department</option>
                            <DepList depList={this.state.depList} />
                        </select>
                        <select name='city' onChange={this.cityChange}>
                            <option value="" disabled selected>City</option>
                            <CityList cityList={this.state.cityList} />
                        </select><br></br>
                        <input
                            type='password'
                            name='password'
                            placeholder='Password'
                            value={this.state.password}
                            onChange={this.onChange}
                        /><br></br>
                        <input
                            type='password'
                            name='confPass'
                            placeholder='Confirm Password'
                            value={this.state.confPass}
                            onChange={this.onChange}
                        /><br></br>
                        <button onClick={this.backHome}>Cancel</button>
                        <input type='submit' value='Sign Up' />
                    </form>
                </div>
            </div>
        )
    }
}

const boxStyle = {
    height: '91vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
}

const formStyle = {
    height: '75%',
    width: '25%',
    alignItems: 'center',
    border: '#005DFF 1px solid',
    borderRadius: '15px',
    backgroundColor: '#29ABE2',
    display: 'flex',
    flexDirection: 'column',
}

export default SignUp
