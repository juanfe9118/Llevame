import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class UserLanding extends Component {
    render() {
        return (
            <div>
                <h2>What do you want to do today?</h2>
                <div style={{display: 'flex', flexDirection: 'column'}}>
                    <Link to='#' >Drive</Link>
                    <Link to='#' >Ride</Link>
                </div>
            </div>
        )
    }
}
