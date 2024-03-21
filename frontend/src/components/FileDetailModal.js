import { Modal, Button, Table } from 'react-bootstrap';

function FileDetailsModal({ show, columns, onHide }) {  
    return (
        <Modal show={show} onHide={onHide} centered>
            <Modal.Header closeButton>
                <Modal.Title>File Details</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Table striped bordered hover>
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Column Name</th>
                            <th>Column Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        {columns.map((column, index) => (
                            <tr key={index}>
                                <td>{index + 1}</td>
                                <td>{column.name}</td>
                                <td>{column.column_type}</td>
                            </tr>
                        ))}
                    </tbody>
                </Table>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={onHide}>Close</Button>
            </Modal.Footer>
        </Modal>
    );
}

export default FileDetailsModal;
