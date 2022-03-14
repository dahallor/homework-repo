	.file	"power_of_two.c"
	.text
	.section	.rodata
.LC0:
	.string	"%d\t%d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$80, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$1, -48(%rbp)
	movl	$2, -44(%rbp)
	movl	$4, -40(%rbp)
	movl	$8, -36(%rbp)
	movl	$16, -32(%rbp)
	movl	$32, -28(%rbp)
	movl	$64, -24(%rbp)
	movl	$1, -64(%rbp)
	jmp	.L2
.L11:
	movl	$0, -60(%rbp)
	movl	-64(%rbp), %eax
	movl	%eax, -56(%rbp)
	movb	$110, -65(%rbp)
.L10:
	movl	$0, -52(%rbp)
	jmp	.L3
.L5:
	movl	-52(%rbp), %eax
	cltq
	movl	-48(%rbp,%rax,4), %eax
	cmpl	%eax, -56(%rbp)
	jne	.L4
	movl	-60(%rbp), %edx
	movl	-64(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movb	$121, -65(%rbp)
.L4:
	addl	$1, -52(%rbp)
.L3:
	cmpl	$7, -52(%rbp)
	jle	.L5
	cmpb	$121, -65(%rbp)
	je	.L15
	movl	-56(%rbp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	jne	.L8
	movl	-56(%rbp), %eax
	movl	%eax, %edx
	shrl	$31, %edx
	addl	%edx, %eax
	sarl	%eax
	movl	%eax, -56(%rbp)
	addl	$1, -60(%rbp)
	jmp	.L9
.L8:
	movl	-56(%rbp), %eax
	andl	$1, %eax
	testl	%eax, %eax
	je	.L10
	movl	-56(%rbp), %edx
	movl	%edx, %eax
	addl	%eax, %eax
	addl	%edx, %eax
	addl	$1, %eax
	movl	%eax, -56(%rbp)
	addl	$1, -60(%rbp)
	nop
.L9:
	jmp	.L10
.L15:
	nop
	addl	$1, -64(%rbp)
.L2:
	cmpl	$100, -64(%rbp)
	jle	.L11
	movl	$0, %eax
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L13
	call	__stack_chk_fail@PLT
.L13:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
