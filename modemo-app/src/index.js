import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import logo from './logo.png';
import * as d3 from "d3";
import './index.css';

const url = "http://localhost:5001"

class Root extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      pageValue: 'Home',
      data: null,
      error: false
    };
    this.changePage = this.changePage.bind(this);
    this.updateData = this.updateData.bind(this);
  }

  changePage(page, errored) {
    this.setState({pageValue: page});
    this.setState({error: errored})
  }

  updateData(data) {
    this.setState({data: data});
  }

  render() {
    let visiblePage = null;
    switch(this.state.pageValue) {
      case 'Home':
        visiblePage = <LandingPage
                        errored={this.state.error}
                        changePage={this.changePage}
                        updateData={this.updateData}/>;
        break;
      case 'Loading':
        visiblePage = <LoadingPage />;
        break;
      case 'Analysis':
        console.log(this.state.data)
        visiblePage = <AnalysisPage data={this.state.data}
                        errored={this.state.error}
                        changePage={this.changePage}
                        updateData={this.updateData}/>;
        break;
      default:
        visiblePage = null;
    }
    return (
      <div className='container'>
        <Header />
        {visiblePage}
      </div>
    );
  }
}

class Header extends React.Component {
  render() {
    return (
      <div className='header'>
        <img src={logo} className='modemo-logo' alt='logo' />
        <h2 className='modemo-title'>modemo</h2>
      </div>
    );
  }
}

class LandingPage extends React.Component {
  render() {
    return (
      <div className='pageContent'>
        {this.props.errored ? <div className="alert alert-danger">There was an error in processing the article.</div> : null}
        <h2 className='title'>Analyze a URL</h2>
        <UrlInput changePage={this.props.changePage} updateData={this.props.updateData}/>
        <p>
          modemo can analyze the political bias of any news article for you.
          Just input the article url of your choice and let Modemo show you the results.
        </p>
      </div>);
  }
}

const LoadingPage = () => (
      <div className='pageContent'>
        <p>
          Analyzing...
        </p>
        <div className="loader"></div>
      </div>
);

class AnalysisPage extends React.Component {
  render() {
    let data = this.props.data.dictionary
    let keys = Object.keys(data);
    console.log(this.props.data.total_bias)
    let bias = this.props.data.total_bias[0] + this.props.data.total_bias[1]
    let values = keys.map(key => data[key])
    let extent = d3.extent(values, d=>d)
    let scale = d3.scaleLinear().domain([extent[0], 0, extent[1]]).range(["#e74c3c", "#fff", "#3498db"])
    let sentScaleColor = d3.scaleLinear().domain([-3, 0, 3]).range(["#e74c3c", "#ddd", "#3498db"])
    let sentScale = d3.scaleQuantile()
      .domain([-3, -1, 0, 1, 3])
      .range(["Strongly Conservative", "Conservative", "Neutral", "Liberal", "Strong Liberal"])
    return (
      <div className='content'>
        <div className='pageContent'>
          <h2 className='title'>Analyze a URL</h2>
          <UrlInput changePage={this.props.changePage} updateData={this.props.updateData}/>
        </div>
        <div className='analysisContent'>
        <div className='analysisHeader'>
          <h2 className='text-stroke' style={{color: sentScaleColor(bias)}}>{sentScale(bias)}</h2>
          <p> Blue sentences indicate more liberal while red sentences are more conservative. Regular sentences are neutral. </p>
        </div>
        {
          keys.map((key, i) => {
            return <span key={i} style={{backgroundColor: scale(data[key])}}>{key}</span>
          })
        }
        </div>
      </div>);
  }
}

class UrlInput extends React.Component {
  constructor(props) {
    super(props);
    this.state = {url: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({url: event.target.value});
  }

  handleSubmit() {
    this.props.changePage("Loading")
    axios.get(url + "/get_dict", {
        params: { url: this.state.url },
        timeout: Number.POSITIVE_INFINITY
    })
    .then(response => {
      this.props.updateData(response.data)
      this.props.changePage("Analysis")
    })
    .catch(error => {
      console.log(error)
      this.props.changePage("Home", true)
    })
  }

  render() {
    return (
      <div>
        <form className='url-input-row'>
          <label>
            <input type='text' value={this.state.url} onChange={this.handleChange} placeholder='Input a URL'/>
          </label>
        </form>
        <button onClick={this.handleSubmit}> Analyze URL </button>
      </div>
    );
  }
}

ReactDOM.render(
  (<Root />),
  document.getElementById('root')
);