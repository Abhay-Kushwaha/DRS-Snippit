import { useState, useEffect } from 'react'
import axios from 'axios'

const Table = () => {
    const [data, setData] = useState([])

    useEffect(() => {
        const fetchData = async () => {
            try {
                let res = await axios.get('http://127.0.0.1:8000/api/emp/')
                if (res.data && res.data.Persons) {
                    console.log("Data: ", res.data.Persons)
                    setData(res.data.Persons)
                }
            } catch (err) {
                console.log("Error: ", err)
            }
        }
        fetchData()
    }, [])

    return (
        <div className='p-15'>
            <h2 className='font-medium text-2xl text-center'>All Employee</h2>
            <table className='w-full table-auto border-2 border-black' border="1">
                <thead className='bg-gray-200'>
                    <tr>
                        <th className='py-2'>ID</th>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Position</th>
                        <th>Country</th>
                        <th>Caste</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody className='bg-white text-center py-10'>
                    {data.map((emp) => (
                        <tr key={emp.id}>
                            <td className='py-2'>{emp.id}</td>
                            <td>{emp.name}</td>
                            <td>{emp.age}</td>
                            <td>{emp.position}</td>
                            <td>{emp.country}</td>
                            <td>{emp.caste?.caste_name}</td>
                            <td>—</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default Table
