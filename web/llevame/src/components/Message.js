import React, { Component } from 'react';
import LoadMessage from './LoadMessage';

export class Message extends Component {
    render() {
        return this.props.messages.map((message) => (
            <LoadMessage key={message.id} message={message} user_id={this.props.user_id} />
        ));
    }
}

export default Message
