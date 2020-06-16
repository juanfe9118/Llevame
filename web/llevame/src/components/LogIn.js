import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';

export class LogIn extends Component {
    state = {
        redirect: null,
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
                    <form onSubmit={this.props.onSubmit}>
                        <input
                            type='email'
                            name='email'
                            placeholder='Email'
                            value={this.state.email}
                            onChange={this.props.onChange}
                        /><br></br>
                        <input
                            type='password'
                            name='password'
                            placeholder='Password'
                            value={this.state.password}
                            onChange={this.props.onChange.bind(this)}
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
