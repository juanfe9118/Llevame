import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class UserLanding extends Component {
    render() {
        return (
            <div style={landingStyle}>
                <div style={divStyle}>
                    <h2 style={{padding: '20px', margin: '30px 0', fontSize: '50px', textAlign: 'center'}}>What do you want to do today?</h2>
                    <div style={{width: '70%', display: 'flex', flexDirection: 'column'}}>
                        <Link style={linkStyle} to='/vehicle' >Drive</Link>
                        <Link style={linkStyle} to='/chats' >Ride</Link>
                    </div>
                </div>
            </div>
        )
    }
}

const landingStyle = {
    height: '91vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
}

const divStyle = {
    height: '75%',
    width: '25%',
    alignItems: 'center',
    border: '#005DFF 1px solid',
    borderRadius: '15px',
    backgroundColor: '#29ABE2',
    display: 'flex',
    flexDirection: 'column',
}

const linkStyle = {
    textAlign: 'center',
    fontSize: '35px',
    margin: '20px 0',
    padding: '10px',
    border: '1px solid #707070',
    borderRadius: '30px',
    backgroundColor: '#B3B3B3',
    color: '#fff',
}