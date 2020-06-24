import React, { Component } from 'react';
import LoadChat from './LoadChat';

export class Chat extends Component {
    render() {
        return this.props.chats.map((chat) => (
            <LoadChat key={chat.id} chat={chat} loadChat={this.props.loadChat} token={this.props.token} user_id={this.props.user_id} />
        ))
    }
}

export default Chat
