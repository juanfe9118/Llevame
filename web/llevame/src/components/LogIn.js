import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import axios from 'axios';

export class LogIn extends Component {
    state = {
        email: '',
        password: '',
        redirect: null,
        token: null,
        user_id: null,
    }

    //When needing information to populate page use mount option to load states
    /* componentDidMount () {
        axios.get()
    }*/

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    onSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/login/', {
            username: this.state.email,
            password: this.state.password
        })
            .then(res => {
                console.log(res.data);
                this.setState({ user_id: res.data.user_id});
                this.setState({ token: res.data.token});
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
                    <h1>Welcome Back!</h1>
                    <form onSubmit={this.onSubmit}>
                        <input
                            type='email'
                            name='email'
                            placeholder='Email'
                            value={this.state.email}
                            onChange={this.onChange}
                        /><br></br>
                        <input
                            type='password'
                            name='password'
                            placeholder='Password'
                            value={this.state.password}
                            onChange={this.onChange}
                        /><br></br>
                        <button onClick={this.backHome}>Cancel</button>
                        <input type='submit' value='Log In' />
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

export default LogIn
