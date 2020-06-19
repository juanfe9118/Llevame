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
            <div id='box'>
                <div id='login'>
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
                        <div id='buttons'>
                            <button onClick={this.backHome}>Cancel</button>
                            <input type='submit' value='Log In' />
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default LogIn
