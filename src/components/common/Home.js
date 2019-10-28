//pic size 687*687
import React from 'react'
import axios from 'axios'
import {Link} from 'react-router-dom'

const pickOTW = Math.floor(Math.random()*12)

class Home extends React.Component{
  constructor(){
    super()
    this.state = {
      data: {},
      error: ''

    }
    this.componentDidMount = this.componentDidMount.bind(this)
  }


  componentDidMount(){
    axios.get('/api/records')
      .then(res => this.setState({ records: res.data }))


  }

  render() {

    console.log(this.state)

    return (
      <div className='container'>

        {this.state.records &&
          <div>
            <div className='title'>
              Record of the Week
            </div>
            <div className='columns is-multiline is-mobile'>
            <div className='column is-4'>
            <figure className="image is-256x256"><img src={this.state.records[pickOTW].cover}></img></figure>
          </div>
            <div className='column'>
              {this.state.records[pickOTW].description}
              </div>
              </div>
            <div className= 'card-header-title'>
              {this.state.records[pickOTW].title}
            </div>
            <div className= 'card-header-title-3'>
              {this.state.records[pickOTW].artist}
            </div>

            <div className='title'>
              New Releases
            </div>
            <div className='columns is-multiline is-mobile'>


              {this.state.records.map(record => {
                return <div className='column is-2' key={record.id}>
                  <Link to={`/records/${record.id}`}> <div  className="card">


                    <div className='card-image'><img src={record.cover}></img></div>
                    <div className= 'card-header-title'>
                      {record.title}
                    </div>
                    <div className= 'card-header-title-3'>
                      {record.artist}
                    </div>

                  </div>
                  </Link>
                </div>

              })}
            </div>
          </div>}


      </div>




    )
  }
}
export default Home
