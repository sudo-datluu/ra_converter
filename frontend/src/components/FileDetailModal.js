import { Modal, Button, ListGroup } from 'react-bootstrap';

function FileDetailsModal({ show, columns, onHide }) {
    return (
        <Modal show={show} onHide={onHide} centered>
            <Modal.Header closeButton>
                <Modal.Title>File Details</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <ListGroup>
                    {columns.map((column, index) => (
                        <ListGroup.Item key={index}>{column.name}</ListGroup.Item> // Adjust as necessary
                    ))}
                </ListGroup>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={onHide}>Close</Button>
            </Modal.Footer>
        </Modal>
    );
}

export default FileDetailsModal;
