import React from 'react';
import SendEmailForm from '../SendEmailForm/SendEmailForm';

class EmailSendingWrapper extends React.Component {
    constructor() {
        super();
        this.state = {
            loading: false,
            statusMessage: null,
        }
    }


    onFormSubmit(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        this.setState({loading: true})
        fetch('/message', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(result => {
            this.setState({
                loading: false,
                statusMessage: {
                    variant: 'success',
                    value: `Email task started with id ${result.task_id}`,
                }
            })
        })
        .catch(error => {
            console.error(error);
            this.setState({
                loading: false,
                statusMessage: {
                    variant: 'danger',
                    value: 'Some error occured',
                }
            })
        })

    }

    render() {
        return (
            <SendEmailForm loading={this.state.loading} onSubmit={this.onFormSubmit.bind(this)} statusMessage={this.state.statusMessage}/>
        )
    }
}

export default EmailSendingWrapper;
