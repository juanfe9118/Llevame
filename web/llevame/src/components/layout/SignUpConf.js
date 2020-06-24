import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';


export class SignUpConf extends Component {
    state = {
        redirect: null,
    }


    toLogIn = () => {
        sleep (5000);
        this.setState({redirect: '/login'});
    }

    render() {
        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />
          }
        return (
            <div id='box'>
                <div id='success'>
                    <h3 on>User successfully created you will be redirected to the log in page shortly.</h3>
                </div>
            </div>
        )
    }
}

export default SignUpConf



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
