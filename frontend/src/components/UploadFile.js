import React, { useState, useEffect } from 'react'
import axios from 'axios'
import FileDetailsModal from './FileDetailModal'
import UploadAlert from './UploadAlert'

function UploadFile() {
    const [filename, setFilename] = useState('')
    const [files, setFiles] = useState([{}])
    const [status, setstatus] = useState('')
    const [uploadStatus, setUploadStatus] = useState(false)
    const [showModal, setShowModal] = useState(false);
    const [columns, setColumns] = useState([]);
    const [selectedFileId, setSelectedFileId] = useState(null);
    const [showAlert, setShowAlert] = useState(false);
    const [alertMessage, setAlertMessage] = useState('');
    const [alertVariant, setAlertVariant] = useState('success');
    let api = 'http://127.0.0.1:8000/api'


    const saveFile = () => {
        let formData = new FormData();
        setUploadStatus(true)
        formData.append("content", filename)

        let axiosConfig = {
            headers: {
                'Content-Type': 'multpart/form-data'
            }
        }

        axios.post(api + '/files/', formData, axiosConfig).then(
            response => {
                setAlertMessage('File Uploaded Successfully');
                setAlertVariant('success');
                setShowAlert(true);
                setUploadStatus(false)
            }
        ).then(getFiles()).catch(error => {
            setShowAlert(true);
            setAlertVariant('danger');
            setAlertMessage(error.response.data['content'].join(', '));
            setUploadStatus(false)
        })
    }


    const getFiles = () => {

        axios.get(api + '/files/').then(
            response => {
                //console.log(response.data)
                setFiles(response.data)
            }
        ).catch(error => {
            console.log(error)
        })

    }

    const forceDownload = (response, title) => {
        console.log(response)
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', title + '.pdf')
        document.body.appendChild(link)
        link.click()


    }

    const downloadWithAxios = (url, title) => {
        axios({
            method: 'get',
            url,
            responseType: 'arraybuffer'
        }).then((response) => {
            forceDownload(response, title)
        }).catch((error) => console.log(error))

    }


    useEffect(() => {
        getFiles()
        console.log(files)
    }, [uploadStatus])

    const fetchFileColumns = (fileId) => {
        axios.get(`${api}/files/${fileId}/columns/`)
            .then(response => {
                setColumns(response.data);
                setSelectedFileId(fileId);
                setShowModal(true);
            })
            .catch(error => console.log(error));
    };

    return (
        <div className="container-fluid">

            <h2 className="text-center alert mt-2">RA Converter</h2>

            <div className="row">
                <div className="col-md-4">
                    <h2 className="alert alert-success">File Upload Section</h2>

                    <form >
                        <div className="form-group">
                            <label htmlFor="exampleFormControlFile1" className="float-left">Browse A File To Upload</label>
                            <input type="file" onChange={e => setFilename(e.target.files[0])} className="form-control" />
                        </div>

                        <button type="button" onClick={saveFile} className="btn btn-primary float-left mt-2">Submit</button>
                        <br />
                        <br />
                        <br />
                    </form>


                </div>


                <div className="col-md-7">


                    <h2 className="alert alert-success">List of Uploaded Files</h2>

                    <table className="table table-bordered mt-4">
                        <thead>
                            <tr>
                                <th scope="col">File Title</th>
                                <th scope="col">Download</th>
                            </tr>
                        </thead>
                        <tbody>

                            {files.map(file => {
                                return (
                                    <tr>
                                        <td class="align-middle">{file.content}</td>
                                        <td><a href="" target="_blank"></a>
                                            <button className='btn btn-success me-4' onClick={() => fetchFileColumns(file.fileID)}>
                                                View Details
                                            </button>

                                            <button onClick={
                                                () => downloadWithAxios(file.content, file.fileID)
                                            } className="btn btn-success">
                                                DownLoad
                                            </button>
                                        </td>
                                    </tr>
                                )
                            })}
                        </tbody>
                    </table>

                </div>
            </div>
            <UploadAlert show={showAlert} message={alertMessage} variant={alertVariant} onClose={() => setShowAlert(false)} />
            <FileDetailsModal show={showModal} columns={columns} onHide={() => setShowModal(false)} />
        </div>
    )
    
}

export default UploadFile