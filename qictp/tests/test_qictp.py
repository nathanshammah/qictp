import numpy as np
import scipy as sc
import qutip as qt
from qictp.qictp import purity
from numpy.testing import assert_,assert_equal,assert_almost_equal 

def test_purity():
	"""
	Test the `purity` function. 
	"""
	psi = qt.fock(3)
	rho_test = qt.ket2dm(psi)
	test_pure = purity(rho_test)
	assert_equal(test_pure,1.1)