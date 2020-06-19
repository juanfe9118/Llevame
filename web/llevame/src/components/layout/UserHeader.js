import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';

export class UserHeader extends Component {
    state = {
        toggleLi: false,
        toggleMenu: false,
        redirect: null,
    }

    changeLi = () => {
        const liState = this.state.toggleLi;
        this.setState({toggleLi: !liState});
    }

    menuTrue = () => this.setState({toggleMenu: true});

    menuFalse = () => this.setState({toggleMenu: false});

    goHistory = () => this.setState({redirect: '/chats'});

    goHome = () => this.setState({redirect: '/userlanding'});

    goProfile = () => this.setState({redirect: '/vehicle'});

    render() {
        if (this.state.redirect) {
            return <Redirect to={this.state.redirect} />
          }
        return (
            <header style={headerStyle}>
                <h1 style={h1Style}>Llévame</h1>
                <div style={divMenu}>
                    <ul>
                        <h3 onClick={this.changeLi} 
                        onMouseEnter={this.menuTrue}
                        onMouseLeave={this.menuFalse}
                        style={this.state.toggleMenu ? menuHover : menuStyle}>
                            Menu
                        </h3>
                        <li style={this.state.toggleLi ? liShow : liHidden} onClick={this.goProfile} >Profile</li>
                        <li style={this.state.toggleLi ? liShow : liHidden} onClick={this.goHistory} >Chat History</li>
                        <li style={this.state.toggleLi ? liShow : liHidden} onClick={this.goHome} >Back to Drive/Ride</li>
                        <li style={this.state.toggleLi ? liShow : liHidden} onClick={this.props.signOut} >Sign Out</li>
                    </ul>
                </div>
            </header>
        )
    }
}

const headerStyle = {
    backgroundColor: '#29ABE2',
    color: '#fff',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between'
}

const h1Style = {
    marginLeft: '50px'
}

const liShow = {
    display: 'block',
    cursor: 'pointer',
}

const liHidden = {
    display: 'none',
    cursor: 'pointer',
}

const menuStyle = {
    padding: '10px 0',
    margin: '5px 50px',
    backgroundColor: 'rgba(112, 112, 112, 0.9)',
    color: '#fff',
    cursor: 'pointer',
    border: '#005DFF 1px solid',
    borderRadius: '50%',
}

const menuHover = {
    padding: '10px 0',
    margin: '5px 50px',
    backgroundColor: 'rgb(112, 112, 112)',
    color: '#fff',
    cursor: 'pointer',
    border: '#005DFF 1px solid',
    borderRadius: '50%',
}

const divMenu = {
    
}

export default UserHeader
