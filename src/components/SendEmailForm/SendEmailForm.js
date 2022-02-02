import { Alert, Button, Col, Container, Form, Row, Spinner } from 'react-bootstrap';
import './SendEmailForm.css';

function SendEmailForm(props) {
    return (
        <Container className="col-md-5 mx-auto mt-10p">
            <Row>
                <Col>
                    <Form onSubmit={props.onSubmit}>
                        <Form.Group className="mb-3" controlId="fromEmail">
                            <Form.Label>From email</Form.Label>
                            <Form.Control type="email" name="from" required/>
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="toEmail">
                            <Form.Label>To email</Form.Label>
                            <Form.Control type="email" name="to" required/>
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="subject">
                            <Form.Label>Subject</Form.Label>
                            <Form.Control name="subject" required/>
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="message">
                            <Form.Label>Message</Form.Label>
                            <Form.Control as="textarea" rows={3} name="message" required/>
                        </Form.Group>
                        {
                            props.statusMessage && (
                                <Alert variant={props.statusMessage.variant}>
                                    {props.statusMessage.value}
                                </Alert>
                            )
                        }
                        {
                            (() => {
                                if(props.loading) {
                                    return (
                                        <Button variant="primary" disabled type="submit">
                                            <Spinner
                                                as="span"
                                                animation="border"
                                                size="sm"
                                            />
                                            <span className='ml-8'>Sending</span>
                                        </Button>
                                    )
                                } else{
                                    return (
                                        <Button variant="primary" type="submit">
                                            Submit
                                        </Button>
                                    )
                                }
                            })()
                        }
                    </Form>
                </Col>
            </Row>
        </Container>
    )
}

export default SendEmailForm;