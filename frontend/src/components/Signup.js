import React from "react";

const Signup = () => {
  return (
    <div className="container mt-5">
      <div className="text-center mb-4">
        <h2>
          <i className="fas fa-user-plus me-2"></i>Signup
        </h2>
        <p className="text-muted">
          Create your account to start tracking expenses
        </p>
      </div>
      <form>
        <div className="">
          <label className="form-label">FullName</label>
          <div className="input-group">
            <span className="input-group-text">
              <i className="fas fa-user"></i>
            </span>
            <input
              type="text"
              name="FullName"
              className="form-control"
              required
              placeholder="Enter your full name"
            />
          </div>
        </div>
      </form>
    </div>
  );
};

export default Signup;
