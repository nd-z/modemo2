import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import logo from './logo.png';
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
        visiblePage = <AnalysisPage data={this.state.data}/>;
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
  constructor(props) {
    super(props);
  }

  render() {
    console.log(this.props)
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
      <div className='analysisContent'>
        <p>
          Analyzing...
        </p>
        <div className="loader"></div>
      </div>
);

class AnalysisPage extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className='pageContent'>
        <h2 className='title'>Analyze a URL</h2>
        <UrlInput changePage={this.props.changePage}/>
        <p>
          modemo can analyze the political bias of any news article for you.
          Just input the article url of your choice and let Modemo show you the results.
        </p>
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
    // axios.post(url + "/analyze", {url: this.state.url})
    // .then(response => {
    //   this.props.changePage("Analysis")
    //   this.props.updateData(response.data)
    // })
    // .catch(error => {
    //   this.props.changePage("Home", true)
    // })
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