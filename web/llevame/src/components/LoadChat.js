import React, { Component } from 'react';
import { Link, Route } from 'react-router-dom';
import Messages from './Messages';  

export class LoadChat extends Component {
    state = {
        chatLink: '/chats/chat_' + this.props.chat.id,
    }

    render() {
        return (
            <div style={boxStyle}>
                <Link to={this.state.chatLink}>Chat # {this.props.chat.id}</Link>
                <Route path={this.state.chatLink} render={props => (
                    <React.Fragment>
                        <Messages messages={this.props.chat.messages} chat={this.props.chat.id} loadChat={this.props.loadChat} token={this.props.token} user_id={this.props.user_id} />
                    </React.Fragment>
                )}
                />
            </div>
        )
    }
}

const boxStyle = {
    height: '91vh',
    display: 'flex',
    justifyContent: 'space-evenly',
    alignItems: 'center',
}

export default LoadChat
