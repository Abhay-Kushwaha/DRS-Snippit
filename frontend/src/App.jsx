import Add from './components/Add'
import Table from './components/Table'
import './App.css'

function App() {

  return (
    <>
      <div>
        <h1 className='font-bold text-4xl py-2 text-center'>Employee Management</h1>
        <div className=''>
          <Add />
          <Table/>
        </div>
      </div>
    </>
  )
}

export default App
