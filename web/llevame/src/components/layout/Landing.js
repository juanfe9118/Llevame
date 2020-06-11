import React from 'react'
import { Link } from 'react-router-dom';

export default function Landing() {
    return (
        <div style={boxStyle}>
            <div style={leftDiv}>
                <h1 style={{fontSize: '50px'}}>Find people with similar destinations and chat with them</h1>
                <h3 style={{fontSize: '25px'}}>Sign up now and get started free!</h3><br></br>
                <Link style={linkStyle} to='#'>Sign Up</Link>
            </div>
            <div style={rightDiv}></div>
        </div>
    )
}

const boxStyle = {
    height: '91vh',
    width: '90vw',
    display: 'flex',
    justifyContent: 'space-evenly',
    alignItems: 'center',
}

const leftDiv = {
    height: '75%',
    width: '25%',
    display: 'flex',
    flexDirection: 'column',
    textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',
}

const rightDiv = {
    height: '75%',
    width: '25%',
    alignItems: 'center',
    border: '#005DFF 1px solid',
    borderRadius: '15px',
    backgroundColor: '#29ABE2',
}

const linkStyle = {
    backgroundColor: '#29ABE2', 
    color: '#fff',
    fontSize: '20px',
    border: '#707070 1px solid',
    borderRadius: '50px',
    padding: '5px 10px',
    margin: '0 10px',
}